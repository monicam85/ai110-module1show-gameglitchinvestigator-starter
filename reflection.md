# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?  
  It looked normal. I didn't notice any issues until attempting to submit a guess and set the difficulty level.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards"). 
  Hints were reversed, when inputting a guess, if it was too low, it told me to go low, and vice versa if it was too high. Also, the get_range_for_difficutly funtion was set so that the hard was easier than normal.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error            |
|-------|-------------------|-----------------|-----------------------------------|
|Guess:3| Go Higher!        | Go Lower        | Out ofattempts! The secret was 23 |
|Normal | Range:1 to 100    | Range: 1 to 50  | Normal Range: 1 to 100            |
|Atempt1| 5 attempts left   | 4 attempts left | First attempt stated at 2         |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
  Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). 
  AI suggested that the hints section be reversed. "Hints are reversed (lines 37-40). guess > secret returns "Go HIGHER!" and guess < secret returns "Go LOWER!". It should be the other way round." I verifed by typing a new guess into the app and getting the expected results. 
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count. 
  In regard to the difficulty level, instead of switching the normal and hard levels, the AL suggested the following: "get_range_for_difficulty: Hard was 1–50, which is easier than Normal. It should be 1–200."

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? 
  By testing it in the application.
- Describe at least one test you ran (manual or using pytest)and what it showed you about your code. 
  If the answer was 23 and I was told to go higher after typing in 3.
- Did AI help you design or understand any tests?Yes How? 
  Claude wrote tests/test_game_logic.py with pytest, with 41 tests covering check_guess, get_range_for_difficulty, parse_guess and update_score. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Imagine Streamlit app as a script that gets re-run from the top every time the user does anything. Whether the the user clicks a button, 
  types in a box, moves a slider,Streamlit runs the entire Python file again from line 1 to the end, then redraws the page with whatever the script produced. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    Always verify that the AI suggestion or fix mated what your expectatons are.
- What is one thing you would do differently next time you work with AI on a coding task?
  I would plan vs automatically accepting fixes.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project changed the way I think about AI generated code in my level of trust for it. I've always assumeed that the AI fixes and answers were always right.
  I have learned the importance of testing and verifying that the AI fixed match the intent of the code. 
