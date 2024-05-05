import pandas as pd
import openai

openai.api_key = ''

# Read in data
input_file = 'data/abstract_text.csv'
df = pd.read_csv(input_file, keep_default_na = False, na_values = '')

def mini_abstract(abstract):
    # Summary prompt
    summary_prompt = f"Summarize the following abstract under 200 words in lay language at a 6th grade reading level, highlighting the study purpose, methods, key findings, and practical importance of these findings for the general public: {abstract}"
    summary_message = openai.ChatCompletion.create(
      model = "gpt-4",
      temperature = 0,
      messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": summary_prompt}
        ]

    )
    summary = summary_message['choices'][0]['message']['content']
    summary_stripped = summary.replace('\n', '')
    abstract_stripped = abstract.replace('\n', '')

    # Fact-check
    fact_check_prompt = f"""Summary: The placebo group had a lower survival rate.
                                Abstract: The placebo group had a higher survival rate.
                                Thought: The summary says the placebo group had worse survival. The abstract says the placebo group had better survival. This is a contradiction.
                                Accurate: False
                                Summary: Those who took aspirin had a quicker drop in their ferritin levels.
                                Abstract: Those who took aspirin had a greater drop in their ferritin levels.
                                Thought: The summary says those who took aspirin had a quicker drop in ferritin. The abstract says they had a greater drop. Quicker and greater are different. The summary has an unsupported statement.
                                Accurate: False
                                Summary: Penicillin is an antibiotic.
                                Abstract: Penicillin is a commonly used antibiotic that can be used for many conditions.
                                Thought: The summary says penicillin is an antibiotic. The abstract says penicillin is an antibiotic. The summary is accurate.
                                Accurate: True
                                Summary: {summary_stripped}
                                Abstract: {abstract_stripped}
                                Thought: <Your Thoughts>
                                Accurate:
                                """
    fact_check_message = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": fact_check_prompt}
        ]
    )
    fact_check_flag = fact_check_message['choices'][0]['message']['content']

    if(fact_check_flag):
        return summary
    else:
        return f"Inaccurate Abstract"

def elevator_pitch(abstract):
    # Summary prompt
    summary_prompt = f"Summarize the following abstract under 100 words in lay language at a 6th grade reading level, highlighting the study purpose, methods, key findings, and practical importance of these findings for the general public: {abstract}"
    summary_message = openai.ChatCompletion.create(
      model = "gpt-4",
      temperature = 0,
      messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": summary_prompt}
        ]

    )
    summary = summary_message['choices'][0]['message']['content']
    summary_stripped = summary.replace('\n', '')
    abstract_stripped = abstract.replace('\n', '')

    # Fact-check
    fact_check_prompt = f"""Summary: The placebo group had a lower survival rate.
                                Abstract: The placebo group had a higher survival rate.
                                Thought: The summary says the placebo group had worse survival. The abstract says the placebo group had better survival. This is a contradiction.
                                Accurate: False
                                Summary: Those who took aspirin had a quicker drop in their ferritin levels.
                                Abstract: Those who took aspirin had a greater drop in their ferritin levels.
                                Thought: The summary says those who took aspirin had a quicker drop in ferritin. The abstract says they had a greater drop. Quicker and greater are different. The summary has an unsupported statement.
                                Accurate: False
                                Summary: Penicillin is an antibiotic.
                                Abstract: Penicillin is a commonly used antibiotic that can be used for many conditions.
                                Thought: The summary says penicillin is an antibiotic. The abstract says penicillin is an antibiotic. The summary is accurate.
                                Accurate: True
                                Summary: {summary_stripped}
                                Abstract: {abstract_stripped}
                                Thought: <Your Thoughts>
                                Accurate:
                                """
    fact_check_message = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": fact_check_prompt}
        ]
    )
    fact_check_flag = fact_check_message['choices'][0]['message']['content']

    if(fact_check_flag):
        return summary
    else:
        return f"Inaccurate Abstract"



for idx, row in list(df.iterrows()):
    abstract = row['abstract']
    mini = mini_abstract(abstract)
    elevator = elevator_pitch(abstract)
    df.at[idx, 'mini_abstract'] = ("").join(mini)
    df.at[idx, 'elevator_pitch'] = ("").join(elevator)
    print(idx)

df.to_csv('abstract_text_summaries.csv')
