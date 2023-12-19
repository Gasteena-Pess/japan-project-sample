class ConversationEvaluator:
    def __init__(self, positive_words, negative_words):
        self.positive_words = set(positive_words)
        self.negative_words = set(negative_words)

    def evaluate_conversation(self, sentences):
        positive_count = 0
        negative_count = 0

        for sentence in sentences:
            words = sentence.lower().split()
            positive_count += sum(word in self.positive_words for word in words)
            negative_count += sum(word in self.negative_words for word in words)

        overall_score = (positive_count - negative_count) / len(sentences)
        return overall_score

# Example conversation sentences
conversation = [
    "I appreciate your hard work on this project.",
    "The team collaboration was excellent.",
    "Unfortunately, there were some misunderstandings in the discussion.",
    "I'm not satisfied with the progress we made.",
]

# Positive and negative words (you can expand or modify these lists)
positive_words = ["appreciate", "excellent", "good", "progress"]
negative_words = ["unfortunately", "misunderstandings", "not satisfied"]

# Create ConversationEvaluator instance
evaluator = ConversationEvaluator(positive_words, negative_words)

# Evaluate the conversation
evaluation_result = evaluator.evaluate_conversation(conversation)

# Print the result
print(f"Conversation Evaluation: {evaluation_result}")
