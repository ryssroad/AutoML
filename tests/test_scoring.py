import unittest
import pytest
from typing import Dict, List

class TestTopKScores(unittest.TestCase):
    def setUp(self):
        # Mock config class to simulate the auditor's config
        class MockConfig:
            def __init__(self):
                self.Auditor = type('obj', (object,), {
                    'top_k': 5,
                    # Generate weights that sum to 1.0 based on top_k
                    'top_k_weights': [1.0/(2**i) for i in range(5)]  # [0.5, 0.25, 0.125, 0.0625, 0.0625]
                })
                
                # Normalize the weights to sum to 1.0
                total = sum(self.Auditor.top_k_weights)
                self.Auditor.top_k_weights = [w/total for w in self.Auditor.top_k_weights]
            
        self.mock_config = MockConfig()
    
    def assert_weights_sum_to_one(self, scores: Dict[str, float]):
        """Helper function to verify weights sum to 1.0 within floating point precision"""
        self.assertAlmostEqual(sum(scores.values()), 1.0, places=5)
    
    def assert_higher_scores_get_higher_weights(self, 
                                              input_scores: Dict[str, float], 
                                              output_weights: Dict[str, float]):
        """Helper function to verify higher scores get higher or equal weights"""
        for hotkey1, score1 in input_scores.items():
            for hotkey2, score2 in input_scores.items():
                if score1 > score2:
                    self.assertGreaterEqual(
                        output_weights[hotkey1], 
                        output_weights[hotkey2],
                        f"Hotkey {hotkey1} with score {score1} should get >= weight than {hotkey2} with score {score2}"
                    )
    
    def assert_equal_scores_get_equal_weights(self, 
                                            input_scores: Dict[str, float], 
                                            output_weights: Dict[str, float]):
        """Helper function to verify equal scores get equal weights"""
        for hotkey1, score1 in input_scores.items():
            for hotkey2, score2 in input_scores.items():
                if abs(score1 - score2) < 1e-5:
                    self.assertAlmostEqual(
                        output_weights[hotkey1],
                        output_weights[hotkey2],
                        places=5,
                        msg=f"Hotkey {hotkey1} and {hotkey2} have equal scores but different weights"
                    )

    def test_all_equal_scores(self):
        """Test when all rovers have the same score"""
        input_scores = {
            f"hotkey_{i}": 0.95 for i in range(8)
        }
        all_hotkeys = list(input_scores.keys())
        
        result = self.calculate_topk_scores(input_scores, all_hotkeys)
        
        # Verify properties
        self.assert_weights_sum_to_one(result)
        self.assert_equal_scores_get_equal_weights(input_scores, result)
        # Each should get 1/8
        expected_weight = 1.0 / 8
        for weight in result.values():
            self.assertAlmostEqual(weight, expected_weight, places=5)

    def test_two_tiers_with_ties(self):
        """Test scenario with two score tiers including ties"""
        input_scores = {
            "hotkey_1": 0.98,
            "hotkey_2": 0.98,  # These two share 0.4
            "hotkey_3": 0.95,
            "hotkey_4": 0.95,  # These two share 0.6
            "hotkey_5": 0.95,
        }
        all_hotkeys = list(input_scores.keys())
        
        result = self.calculate_topk_scores(input_scores, all_hotkeys)
        
        # Verify properties
        self.assert_weights_sum_to_one(result)
        self.assert_higher_scores_get_higher_weights(input_scores, result)
        self.assert_equal_scores_get_equal_weights(input_scores, result)
        
        # Verify specific weights
        self.assertAlmostEqual(result["hotkey_1"], 0.2)  # 0.4/2
        self.assertAlmostEqual(result["hotkey_2"], 0.2)  # 0.4/2
        self.assertAlmostEqual(result["hotkey_3"], 0.2)  # 0.6/3
        self.assertAlmostEqual(result["hotkey_4"], 0.2)  # 0.6/3
        self.assertAlmostEqual(result["hotkey_5"], 0.2)  # 0.6/3

    def test_more_than_k_at_same_tier(self):
        """Test handling of more than k rovers at the same tier"""
        input_scores = {
            "hotkey_1": 0.98,
            "hotkey_2": 0.98,  # These two share 0.4
            "hotkey_3": 0.95,
            "hotkey_4": 0.95,
            "hotkey_5": 0.95,
            "hotkey_6": 0.95,
            "hotkey_7": 0.95,
            "hotkey_8": 0.95,  # These six share 0.6
            "hotkey_9": 0.90,  # Gets 0
            "hotkey_10": 0.90,  # Gets 0
        }
        all_hotkeys = list(input_scores.keys())
        
        result = self.calculate_topk_scores(input_scores, all_hotkeys)
        
        # Verify properties
        self.assert_weights_sum_to_one(result)
        self.assert_higher_scores_get_higher_weights(input_scores, result)
        self.assert_equal_scores_get_equal_weights(input_scores, result)
        
        # Verify specific weights
        self.assertAlmostEqual(result["hotkey_1"], 0.2)  # 0.4/2
        self.assertAlmostEqual(result["hotkey_2"], 0.2)  # 0.4/2
        self.assertAlmostEqual(result["hotkey_3"], 0.1)  # 0.6/6
        self.assertAlmostEqual(result["hotkey_8"], 0.1)  # 0.6/6
        self.assertEqual(result["hotkey_9"], 0.0)  # No weight left
        self.assertEqual(result["hotkey_10"], 0.0)  # No weight left

    def test_zero_scores(self):
        """Test handling of zero scores"""
        input_scores = {
            "hotkey_1": 0.98,
            "hotkey_2": 0.0,
            "hotkey_3": 0.95,
            "hotkey_4": 0.0,
        }
        all_hotkeys = list(input_scores.keys())
        
        result = self.calculate_topk_scores(input_scores, all_hotkeys)
        
        # Verify zero scores get zero weight
        self.assertEqual(result["hotkey_2"], 0.0)
        self.assertEqual(result["hotkey_4"], 0.0)
        
        # Verify total still sums to 1
        self.assert_weights_sum_to_one(result)

    def test_empty_scores(self):
        """Test handling of empty input"""
        result = self.calculate_topk_scores({}, ["hotkey_1", "hotkey_2"])
        
        # Should return zeros for all hotkeys
        self.assertEqual(result["hotkey_1"], 0.0)
        self.assertEqual(result["hotkey_2"], 0.0)
        self.assert_weights_sum_to_one(result)

if __name__ == '__main__':
    unittest.main()