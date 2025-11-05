import streamlit as st
import random
import textwrap

# -------------------------------------------------------
# 🧠 Kelly — The AI-Skeptic Scientist Poet
# -------------------------------------------------------
# A poetic chatbot that responds with analytical,
# skeptical, and evidence-based reflections on AI.
# -------------------------------------------------------

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Kelly — AI-Skeptic Poet",
    page_icon="🧠",
    layout="centered",
)

# -----------------------------
# Header Section
# -----------------------------
st.title("🧠 Kelly — The AI-Skeptic Scientist Poet")
st.markdown(
    """
    *Every answer is a poem — skeptical, analytical, and evidence-based.*

    Kelly questions broad claims about AI, highlights its limits,  
    and offers practical, evidence-grounded suggestions.
    ---
    """
)

# -----------------------------
# Poem Generation Function
# -----------------------------
def generate_kelly_poem(prompt: str) -> str:
    """Generate a skeptical, analytical poem in Kelly’s style."""
    q = prompt.strip()

    # --- Core poetic components ---
    skepticism = [
        "Claim first, evidence later — beware the polished curve.",
        "Numbers alone do not prove truth; they paint a pattern that invites questioning.",
        "A neat demo is not a robust claim; ask for data slices, failure modes, and edge cases.",
        "Metrics hide assumptions. When was the data gathered? What was filtered out?",
    ]

    limitations = [
        "Training bias persists: representative data is brittle when environments shift.",
        "Spurious correlations masquerade as understanding; causal testing is rare and costly.",
        "Adversarial and distributional shifts expose brittle decision surfaces.",
        "Interpretability remains incomplete — explanations often rationalize, not reveal.",
    ]

    suggestions = [
        "Request ablation studies and raw confusion matrices; prefer open evaluation sets.",
        "Run slice-based audits: rare classes, temporal splits, and OOD benchmarks.",
        "Instrument systems in production: log inputs, failures, and human review loops.",
        "Use pre-registered evaluation plans and publish negative results as a rule.",
    ]

    # --- Topic detection ---
    lower = q.lower()
    topics = []
    if any(x in lower for x in ["ethic", "moral", "bias", "fair"]):
        topics.append("ethics")
    if any(x in lower for x in ["audit", "evaluate", "test", "benchmark", "robust"]):
        topics.append("evaluation")
    if any(x in lower for x in ["deploy", "ops", "production", "scal"]):
        topics.append("deployment")
    if any(x in lower for x in ["replace", "job", "work", "econom"]):
        topics.append("impact")
    if any(x in lower for x in ["model", "architecture", "transformer", "vision", "nlp", "llm"]):
        topics.append("technical")
    if not topics:
        topics.append("general")

    # --- Contextual addendum ---
    if "ethics" in topics:
        addendum = "Ask who bears risk, who benefits, and what redress exists for harms."
    elif "evaluation" in topics:
        addendum = "Demand reproducible code, dataset provenance, and multiple baselines."
    elif "deployment" in topics:
        addendum = "Test for concept drift, set rollback criteria, and monitor human feedback loops."
    elif "impact" in topics:
        addendum = "Quantify which tasks change and plan retraining or safety nets accordingly."
    elif "technical" in topics:
        addendum = "Probe inductive biases — what architecture assumptions drive behavior?"
    else:
        addendum = "Be modest with conclusions: seek replication and independent verification."

    # --- Practical checklist ---
    checklist = [
        "1️⃣ Demand open data or provenance.",
        "2️⃣ Test robustness across slices and time.",
        "3️⃣ Use incremental rollouts with oversight.",
        "4️⃣ Publish negative results too.",
    ]

    # --- Compose poem ---
    poem = f"""
    **You asked:** *{q}*

    **Skepticism:** {random.choice(skepticism)}

    **Limitations:** {random.choice(limitations)}

    **Practical Suggestions:** {random.choice(suggestions)}

    **On Your Topic:** {addendum}

    **Checklist:**
    {chr(10).join(checklist)}
    """

    return textwrap.dedent(poem)


# -----------------------------
# Chat Interface
# -----------------------------
if "chat" not in st.session_state:
    st.session_state.chat = []
if "input" not in st.session_state:
    st.session_state.input = ""

# Input prompt
prompt = st.text_input("💬 Ask Kelly a question about AI:", value=st.session_state.input)

# Button handler
if st.button("Ask"):
    if prompt.strip():
        answer = generate_kelly_poem(prompt)
        st.session_state.chat.append(("You", prompt))
        st.session_state.chat.append(("Kelly", answer))
        st.session_state.input = ""  # clear input box after asking
        st.rerun()  # refresh UI to show new chat

# Display conversation history
for who, msg in st.session_state.chat:
    if who == "You":
        st.markdown(f"**🧑‍🎓 {who}:** {msg}")
    else:
        st.markdown(f"**🤖 {who}:** {msg}")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption(
    "Built with ❤️ using Streamlit — all responses are locally generated. "
    "No external APIs or model calls are used."
)
