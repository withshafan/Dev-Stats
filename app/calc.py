def calc_language_stats(repos):
    lang_count = {}
    for repo in repos:
        lang = repo.get("language")
        if lang:
            lang_count[lang] = lang_count.get(lang, 0) + 1

    total = sum(lang_count.values())
    if total == 0:
        return {}

    return {
        lang: round((count / total) * 100, 2)
        for lang, count in sorted(lang_count.items(),
                                   key=lambda x: x[1], reverse=True)
    }

def calc_engagement(repos):
    total_stars = sum(r.get("stargazers_count", 0) for r in repos)
    total_forks = sum(r.get("forks_count", 0) for r in repos)
    return total_stars, total_forks

def prepare_repo_data(user_id, repos):
    return [
        (
            user_id,
            r.get("name", ""),
            r.get("language", "Unknown"),
            r.get("stargazers_count", 0)
        )
        for r in repos
    ]