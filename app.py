import oss
import pandas as pd
import streamlit as st

from core.pipeline import (
    AutoMLPipeline
)
from core.detector import suggest_target_column


st.set_page_config(
    page_title="Agentic AutoML",
    page_icon="🤖",
    layout="wide"
)


st.title(
    "🤖 Agentic AutoML AI"
)

st.caption(
    "Agno + Gemini + Pandas + "
    "Scikit-learn"
)


uploaded = st.file_uploader(
    "Upload your dataset",
    type=["csv", "xlsx"]
)


if uploaded:

    os.makedirs(
        "data/uploads",
        exist_ok=True
    )

    file_path = os.path.join(
        "data/uploads",
        uploaded.name
    )

    with open(
        file_path,
        "wb"
    ) as f:

        f.write(
            uploaded.getbuffer()
        )

    # Preview

    if uploaded.name.endswith(".csv"):

        df = pd.read_csv(
            file_path
        )

    else:

        df = pd.read_excel(
            file_path
        )

    st.subheader(
        "📊 Dataset Preview"
    )

    st.dataframe(
        df.head(20),
        width="stretch"
    )

    st.write(
        f"Rows: {df.shape[0]}"
    )

    st.write(
        f"Columns: {df.shape[1]}"
    )

    # Target

    target = st.selectbox(
        "🎯 Select Target Column",
        df.columns,
        index=list(df.columns).index(suggest_target_column(df))
    )

    if st.button(
        "🚀 Start Agentic AutoML",
        type="primary"
    ):

        with st.status(
            "AI AutoML is working...",
            expanded=True
        ):

            st.write(
                "🔍 Analyzing dataset..."
            )

            pipeline = (
                AutoMLPipeline()
            )

            state = pipeline.run(
                file_path,
                target
            )

            st.write(
                "🧹 Cleaning completed"
            )

            st.write(
                "📈 EDA completed"
            )

            st.write(
                "🤖 Models trained"
            )

            st.write(
                "📊 Evaluation completed"
            )

            st.write(
                "🧠 AI report generated"
            )

        # =========================
        # DATASET
        # =========================

        st.header(
            "📊 Dataset Analysis"
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Rows",
            state.profile["rows"]
        )

        c2.metric(
            "Columns",
            state.profile["columns"]
        )

        c3.metric(
            "Duplicates",
            state.profile["duplicates"]
        )

        # =========================
        # TARGET
        # =========================

        st.header(
            "🎯 Problem Detection"
        )

        st.info(
            f"Target: {state.target}"
        )

        st.info(
            f"Problem: {state.problem_type}"
        )

        # =========================
        # CLEANING
        # =========================

        st.header(
            "🧹 Cleaning Results"
        )

        st.json(
            state.cleaning_report
        )

        # =========================
        # EDA
        # =========================

        st.header(
            "📈 EDA"
        )

        for chart in state.charts:

            st.image(
                chart
            )

        # =========================
        # MODELS
        # =========================

        st.header(
            "🤖 Model Comparison"
        )

        results_df = pd.DataFrame(
            state.model_results
        )

        st.dataframe(
            results_df,
            width="stretch"
        )

        # =========================
        # BEST MODEL
        # =========================

        st.header(
            "🏆 Best Model"
        )

        st.success(
            state.best_model_name
        )

        best_result = next(
            result
            for result in state.model_results
            if result.get("model") == state.best_model_name
            and "error" not in result
        )

        metric_1, metric_2 = st.columns(2)

        if state.problem_type == "classification":
            metric_1.metric(
                "Accuracy",
                f"{best_result['accuracy']:.2%}"
            )
            metric_2.metric(
                "F1 score",
                f"{best_result['f1']:.4f}"
            )
        else:
            metric_1.metric(
                "MSE",
                f"{best_result['mse']:.4f}"
            )
            metric_2.metric(
                "R²",
                f"{best_result['r2']:.4f}"
            )

        # =========================
        # REPORT
        # =========================

        st.header(
            "🧠 AI Generated Report"
        )

        st.markdown(
            state.report
        )
