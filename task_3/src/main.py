import timeit
from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search


def read_article(file_info):
    try:
        filename, encoding = file_info
        with open(filename, "r", encoding=encoding) as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""


def benchmark_algorithm(algorithm_func, text, pattern, num_runs=1000):
    def wrapper():
        return algorithm_func(text, pattern)

    try:
        total_time = timeit.timeit(wrapper, number=num_runs)
        avg_time = total_time / num_runs
        return avg_time, total_time
    except Exception as e:
        print(f"Error benchmarking {algorithm_func.__name__}: {e}")
        return None, None


def main():
    article1_path = ("docs/стаття 1.txt", "Windows-1251")
    article2_path = ("docs/стаття 2.txt", "utf-8-sig")

    article1 = read_article(article1_path)
    article2 = read_article(article2_path)

    if not article1 or not article2:
        print("Failed to read articles")
        return

    existing_patterns = {
        "article1": ["пошук", "алгоритм", "дерево"],
        "article2": ["структури даних", "рекомендаційної", "експериментів"],
    }

    non_existing_patterns = {
        "article1": ["xyzabc123", "qwerty99999", "notfound"],
        "article2": ["fakepattern", "nosuchstring", "xyz999"],
    }

    algorithms = {
        "Boyer-Moore": boyer_moore_search,
        "KMP": kmp_search,
        "Rabin-Karp": rabin_karp_search,
    }

    for pattern_type, patterns in [
        ("Existing Patterns", existing_patterns),
        ("Non-Existing Patterns", non_existing_patterns),
    ]:
        print(f"\n--- {pattern_type} ---")
        for article_key, pats in patterns.items():
            article_text = article1 if article_key == "article1" else article2
            print(f"\nArticle: {article_key}")
            for pattern in pats:
                print(f"\nPattern: '{pattern}'")
                for algo_name, algo_func in algorithms.items():
                    avg_time, total_time = benchmark_algorithm(
                        algo_func, article_text, pattern
                    )
                    if avg_time is not None:
                        print(
                            f"{algo_name}: Avg Time = {avg_time:.10f}s, Total Time = {total_time:.10f}s"
                        )


if __name__ == "__main__":
    main()
