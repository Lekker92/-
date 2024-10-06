# # Διαλογικά Συστήματα και Φωνητικοί Βοηθοί (M913)
# Assignment 3
# Andreas Lekkas (lt12100016)


## Changes Implemented

### 1. Rasa Forms
We updated the "Book a Ticket" scenario to use a Rasa form. The form collects the `destination` and `departure_date` slots from the user. It handles invalid inputs by using fallback actions and gracefully handles chit-chat.

### 2. Policies
We experimented with the following policies:

- **MemoizationPolicy**: Memorizes exact conversation paths. It worked well when the user followed the predefined conversation flow but struggled when the conversation deviated from the training stories.
- **RulePolicy**: This policy worked well for handling forms and fallback behavior as the rules are explicitly defined.
- **TEDPolicy**: This policy performed best for more flexible conversations where the user provided information in an unexpected order or asked additional questions.

### 3. Optimized Policy
The best results were obtained using the **TEDPolicy** due to its ability to generalize to unseen dialogues. We optimized it by increasing the `epochs` to 100 and setting the `max_history` to 5, allowing the bot to better handle varied dialogues.

### Test Cases

1. **Book a Ticket (Happy Path)**: The user books a ticket to London, and the bot asks for the departure date.
2. **Invalid Input Handling**: The user provides irrelevant input during form filling (e.g., chit-chat), and the bot responds with focused messages.
3. **Flexible Input**: The user provides the destination and departure date in a non-standard order, and the bot successfully processes the information.
4. **Goodbye**: The user says "bye," and the bot responds with an appropriate farewell message.
