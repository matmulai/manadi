def format_prompt(prompt: str) -> str:
    """Cleans and formats the user prompt."""
    return prompt.strip()

def format_response(response: str) -> str:
    """Cleans and formats the model response."""
    return response.strip()

def format_feedback(feedback: str) -> str:
    """Cleans and formats the user feedback."""
    return feedback.strip() if feedback else None

def validate_entry(prompt: str, response: str) -> bool:
    """Validates that the prompt and response are not empty."""
    return bool(prompt.strip()) and bool(response.strip())
