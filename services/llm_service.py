from langchain.chains import LLMChain
from langchain_huggingface import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from llm_config  import MODEL_ID, TASK, MODEL_PARAMS
from templates import *

def _get_model() -> HuggingFacePipeline:
    model = HuggingFacePipeline.from_model_id(
        model_id=MODEL_ID,
        task=TASK,
        pipeline_kwargs=MODEL_PARAMS
    )
    
    return model

def invoke_model():
    model = _get_model()
    template = PromptTemplate(
        input_variables=["role", "rules", "categories", "mail"],
        template="""

        Role: {role}

        Rules: {rules}

        Categories: {categories}

        Mail: {mail}

        Category:
"""
    )

    formatted_prompt = template.format(
            categories="\n".join(f"- {cat}" for cat in ["CONFIDENTIAL", "FINANCIAL", "SALES_REPORT"]),
            role=ROLE_ASSISTANT,
            mail=EMAIL_TEST,
            rules=RULES
    )

    return model.invoke(formatted_prompt).split("Category:")[-1].split("\n")[-1]


print(invoke_model())
