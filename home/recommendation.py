from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommend_internships(user_skills, internships, top_n=6):
    """
    user_skills: string
    internships: queryset
    """

    if not user_skills:
        return internships[:top_n]

    internship_skills = [i.skills for i in internships]

    documents = [user_skills] + internship_skills

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])[0]

    ranked_internships = sorted(
        zip(internships, similarity_scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [internship for internship, score in ranked_internships[:top_n]]
