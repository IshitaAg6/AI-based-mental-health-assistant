import pathway as pw
from src.sentiment_analysis import analyze_sentiment

journal_data_source = pw.io.fs.read(
    "./journal_entries/",
    format="binary",
    with_metadata=True,
    mode="streaming"
)

class MentalHealthProcessor(pw.Transformer):
    def transform(self, journal_entry):
        sentiment = analyze_sentiment(journal_entry['text'])
        return {
            "text": journal_entry['text'],
            "sentiment": sentiment
        }

pipeline = pw.Pipeline(journal_data_source, MentalHealthProcessor())
pipeline.run_server()
