# https://luca-bindi.medium.com/oracle23ai-simplifies-rag-implementation-for-enterprise-llm-interaction-in-enterprise-solutions-d865dacdd1ed

import sys

from oci_model_wrapper import OCIModelWrapper

n = len(sys.argv)
if n == 1:
    vector_store = "chroma"
else:
    vector_store = sys.argv[1]

oci_wrapper = OCIModelWrapper()

match vector_store:
    case "ora23ai":
        oci_wrapper.persist_ora23ai_vs()
    case "chroma":
        oci_wrapper.persist_chroma_vs()
    case "faiss":
        oci_wrapper.persist_faiss_vs()

print('\nSuccessfully embedded documents into vector store.')