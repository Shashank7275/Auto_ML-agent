from core.state import AutoMLState
from core.detector import detect_problem_type

from tools.data_tools import (
    load_dataset,
    get_profile
)

from tools.cleaning_tools import (
    clean_dataset
)

from tools.eda_tools import (
    create_eda
)

from tools.model_tools import (
    train_models
)

from agent.data_agent import (
    data_agent
)

from agent.target_agent import (
    target_agent
)

from agent.cleaning_agent import (
    cleaning_agent
)

from agent.model_agent import (
    model_agent
)

from agent.report_agent import (
    report_agent
)


class AutoMLPipeline:

    def run(
        self,
        file_path,
        target
    ):

        state = AutoMLState()

        # =========================
        # LOAD
        # =========================

        df = load_dataset(
            file_path
        )

        state.df = df
        state.file_path = file_path

        # =========================
        # DATA ANALYSIS
        # =========================

        profile = get_profile(df)

        state.profile = profile

        data_ai = data_agent.run(
            f"""
            Analyze this dataset:

            {profile}
            """
        )

        # =========================
        # TARGET
        # =========================

        if target not in df.columns:

            raise ValueError(
                f"Target '{target}' not found."
            )

        problem_type = (
            detect_problem_type(
                df,
                target
            )
        )

        state.target = target
        state.problem_type = problem_type

        target_ai = target_agent.run(
            f"""
            Target:
            {target}

            Problem:
            {problem_type}

            Profile:
            {profile}
            """
        )

        # =========================
        # CLEAN
        # =========================

        df, cleaning_report = (
            clean_dataset(df)
        )

        state.df = df
        state.cleaning_report = (
            cleaning_report
        )

        cleaning_ai = cleaning_agent.run(
            f"""
            Explain these cleaning results:

            {cleaning_report}
            """
        )

        # =========================
        # EDA
        # =========================

        charts = create_eda(df)

        state.charts = charts

        # =========================
        # MODEL
        # =========================

        results, best_name, best_model = (
            train_models(
                df,
                target,
                problem_type
            )
        )

        state.model_results = results
        state.best_model_name = best_name
        state.best_model = best_model

        model_ai = model_agent.run(
            f"""
            Analyze these ML results:

            {results}

            Selected model:
            {best_name}
            """
        )

        # =========================
        # REPORT
        # =========================

        report_ai = report_agent.run(
            f"""
            Generate final AutoML report.

            DATA:
            {profile}

            TARGET:
            {target}

            PROBLEM:
            {problem_type}

            CLEANING:
            {cleaning_report}

            MODELS:
            {results}

            BEST MODEL:
            {best_name}

            DATA ANALYSIS:
            {data_ai.content}

            TARGET ANALYSIS:
            {target_ai.content}

            CLEANING ANALYSIS:
            {cleaning_ai.content}

            MODEL ANALYSIS:
            {model_ai.content}
            """
        )

        state.report = (
            report_ai.content
        )

        return state