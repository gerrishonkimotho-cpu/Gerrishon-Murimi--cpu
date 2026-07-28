"""
Example usage of the G Analysis Tool
"""

from g_analysis_tool import DerivativesAnalyzer
import json


def main():
    """Run example analysis."""
    
    # Initialize analyzer
    analyzer = DerivativesAnalyzer()
    
    # Example 1: Market Analysis
    print("=" * 50)
    print("Example 1: Market Analysis")
    print("=" * 50)
    
    market_data = {
        "price": [100, 102, 101, 105, 103, 107, 106, 108, 110, 109],
        "volume": [1000, 1200, 950, 1500, 1100, 1300, 1250, 1400, 1600, 1550],
    }
    
    market_results = analyzer.analyze_market(market_data)
    print("\nMarket Metrics:")
    print(json.dumps(market_results["market_metrics"], indent=2))
    print("\nTrends:")
    print(json.dumps(market_results["trends"], indent=2))
    
    # Example 2: Matches and Differs Analysis
    print("\n" + "=" * 50)
    print("Example 2: Matches and Differs Analysis")
    print("=" * 50)
    
    data1 = [1.0, 2.0, 3.0, 4.0, 5.0]
    data2 = [1.01, 2.05, 3.0, 4.02, 5.1]
    
    matches = analyzer.find_matches(data1, data2, threshold=0.1)
    print("\nMatches:")
    print(f"Total matches: {matches['total_matches']}")
    print(f"Match percentage: {matches['match_percentage']:.2f}%")
    
    differs = analyzer.find_differs(data1, data2, threshold=0.05)
    print("\nDiffers:")
    print(f"Total differs: {differs['total_differs']}")
    print(f"Differ percentage: {differs['differ_percentage']:.2f}%")
    
    # Example 3: Over/Under Analysis
    print("\n" + "=" * 50)
    print("Example 3: Over/Under Analysis")
    print("=" * 50)
    
    prices = [98, 102, 105, 99, 103, 107, 101, 104, 108, 100]
    threshold = 102
    labels = [f"Day_{i+1}" for i in range(len(prices))]
    
    over_under = analyzer.analyze_over_under(prices, threshold, labels)
    print(f"\nThreshold: {threshold}")
    print(f"Over count: {over_under['over_count']}")
    print(f"Under count: {over_under['under_count']}")
    print(f"Over percentage: {over_under['over_percentage']:.2f}%")
    
    # Example 4: Even/Odd Analysis
    print("\n" + "=" * 50)
    print("Example 4: Even/Odd Analysis")
    print("=" * 50)
    
    contract_numbers = [101, 102, 103, 104, 105, 106, 107, 108]
    
    even_odd = analyzer.analyze_even_odd(contract_numbers)
    print(f"\nEven count: {even_odd['even_count']}")
    print(f"Odd count: {even_odd['odd_count']}")
    print(f"Even percentage: {even_odd['even_percentage']:.2f}%")
    print(f"Odd percentage: {even_odd['odd_percentage']:.2f}%")
    
    # Example 5: Statistical Summary
    print("\n" + "=" * 50)
    print("Example 5: Statistical Summary")
    print("=" * 50)
    
    returns = [-0.02, 0.01, 0.03, -0.01, 0.02, 0.04, -0.03, 0.025]
    
    stats = analyzer.get_statistical_summary(returns)
    print("\nStatistical Summary:")
    print(f"Count: {stats['count']}")
    print(f"Mean: {stats['mean']:.4f}")
    print(f"Median: {stats['median']:.4f}")
    print(f"Std Dev: {stats['std_dev']:.4f}")
    print(f"Min: {stats['min']:.4f}")
    print(f"Max: {stats['max']:.4f}")
    print(f"Skewness: {stats['skewness']:.4f}")
    
    # Example 6: Distribution Comparison
    print("\n" + "=" * 50)
    print("Example 6: Distribution Comparison")
    print("=" * 50)
    
    call_prices = [10, 11, 12, 13, 14, 15, 16, 17, 18]
    put_prices = [9, 10, 11, 12, 13, 14, 15, 16, 17]
    
    comparison = analyzer.compare_distributions(call_prices, put_prices)
    print("\nDistribution Comparison:")
    print(f"Call Mean: {comparison['data1_summary']['mean']:.2f}")
    print(f"Put Mean: {comparison['data2_summary']['mean']:.2f}")
    print(f"Mean Difference: {comparison['mean_difference']:.2f}")
    print(f"T-test p-value: {comparison['t_test']['p_value']:.4f}")
    print(f"Significantly Different: {comparison['t_test']['significantly_different']}")


if __name__ == "__main__":
    main()
