def analyze_scores(scores):
    if not scores:
        return 0, 0, 0
    
    total_sum = 0
    maximum = scores[0]
    minimum = scores[0]
    
    for score in scores:
        total_sum += score
        if score > maximum:
            maximum = score
        if score < minimum:
            minimum = score
            
    average = total_sum / len(scores)
    return total_sum, average, maximum, minimum

if __name__ == "__main__":
    test_scores = [85, 92, 78, 99, 88]
    total, avg, highest, lowest = analyze_scores(test_scores)
    print(f"Total: {total}, Average: {avg}, Highest: {highest}, Lowest: {lowest}")