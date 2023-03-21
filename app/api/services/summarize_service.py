from transformers import AutoTokenizer, BartForConditionalGeneration


class SummarizeService():
	def __init__(self):
		self.model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
		self.tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")

	def summarize_text(self, text_to_summarize, max_length=1500):
		inputs = self.tokenizer([text_to_summarize], max_length=1024, return_tensors="pt", padding='max_length', truncation=True)
		summary_ids = self.model.generate(inputs["input_ids"], num_beams=2, min_length=0, max_length=max_length)
		return self.tokenizer.batch_decode(
			summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
		)[0]
