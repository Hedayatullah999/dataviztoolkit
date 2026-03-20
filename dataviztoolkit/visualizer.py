import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class DataVisualizer:

    def __init__(self, filepath=None, dataframe=None):
        """Load data from a CSV file or directly from a DataFrame."""
        if dataframe is not None:
            self.df = dataframe
        elif filepath is not None:
            self.df = pd.read_csv(filepath)
            print(f"Data loaded successfully")
            print(f"Rows: {self.df.shape[0]}, Columns: {self.df.shape[1]}")
        else:
            raise ValueError("Provide either a filepath or a dataframe.")

    # ─────────────────────────────────────────
    # HISTOGRAM
    # ─────────────────────────────────────────

    def histogram(self, column, bins=20, color="steelblue", title=None, figsize=(8, 5)):
        """
        Plot a histogram for a numeric column.

        Parameters:
            column  : column name to plot
            bins    : number of bins (default 20)
            color   : bar color (default steelblue)
            title   : chart title (optional)
            figsize : figure size (default (8, 5))
        """
        if column not in self.df.columns:
            print(f"Column '{column}' not found.")
            return

        fig, ax = plt.subplots(figsize=figsize)
        ax.hist(self.df[column].dropna(), bins=bins, color=color, edgecolor="white")
        ax.set_title(title if title else f"Histogram — {column}", fontsize=14)
        ax.set_xlabel(column, fontsize=12)
        ax.set_ylabel("Frequency", fontsize=12)
        ax.grid(axis="y", alpha=0.3)
        plt.tight_layout()
        plt.show()
        print(f"Histogram plotted for '{column}'")

    # ─────────────────────────────────────────
    # SCATTER PLOT
    # ─────────────────────────────────────────

    def scatter(self, x, y, color="steelblue", alpha=0.7, title=None, figsize=(8, 5)):
        """
        Plot a scatter plot between two numeric columns.

        Parameters:
            x       : column name for x-axis
            y       : column name for y-axis
            color   : dot color (default steelblue)
            alpha   : transparency (default 0.7)
            title   : chart title (optional)
            figsize : figure size (default (8, 5))
        """
        for col in [x, y]:
            if col not in self.df.columns:
                print(f"Column '{col}' not found.")
                return

        fig, ax = plt.subplots(figsize=figsize)
        ax.scatter(self.df[x], self.df[y], color=color, alpha=alpha, edgecolors="white", linewidths=0.5)
        ax.set_title(title if title else f"Scatter Plot — {x} vs {y}", fontsize=14)
        ax.set_xlabel(x, fontsize=12)
        ax.set_ylabel(y, fontsize=12)
        ax.grid(alpha=0.3)
        plt.tight_layout()
        plt.show()
        print(f"Scatter plot plotted for '{x}' vs '{y}'")

    # ─────────────────────────────────────────
    # BAR CHART
    # ─────────────────────────────────────────

    def bar_chart(self, column, top_n=10, color="steelblue", title=None, figsize=(8, 5), horizontal=False):
        """
        Plot a bar chart showing value counts for a categorical column.

        Parameters:
            column     : column name to plot
            top_n      : show only top N values (default 10)
            color      : bar color (default steelblue)
            title      : chart title (optional)
            figsize    : figure size (default (8, 5))
            horizontal : if True, plot horizontal bars (default False)
        """
        if column not in self.df.columns:
            print(f"Column '{column}' not found.")
            return

        counts = self.df[column].value_counts().head(top_n)

        fig, ax = plt.subplots(figsize=figsize)

        if horizontal:
            ax.barh(counts.index.astype(str), counts.values, color=color, edgecolor="white")
            ax.set_xlabel("Count", fontsize=12)
            ax.set_ylabel(column, fontsize=12)
            ax.invert_yaxis()
        else:
            ax.bar(counts.index.astype(str), counts.values, color=color, edgecolor="white")
            ax.set_xlabel(column, fontsize=12)
            ax.set_ylabel("Count", fontsize=12)
            plt.xticks(rotation=45, ha="right")

        ax.set_title(title if title else f"Bar Chart — {column}", fontsize=14)
        ax.grid(axis="y" if not horizontal else "x", alpha=0.3)
        plt.tight_layout()
        plt.show()
        print(f"Bar chart plotted for '{column}'")

    # ─────────────────────────────────────────
    # HEATMAP
    # ─────────────────────────────────────────

    def heatmap(self, cmap="coolwarm", title=None, figsize=(10, 8), annot=True):
        """
        Plot a correlation heatmap for all numeric columns.

        Parameters:
            cmap    : colormap (default coolwarm)
            title   : chart title (optional)
            figsize : figure size (default (10, 8))
            annot   : show correlation values (default True)
        """
        numeric_df = self.df.select_dtypes(include="number")

        if numeric_df.empty:
            print("No numeric columns found for heatmap.")
            return

        corr = numeric_df.corr()

        fig, ax = plt.subplots(figsize=figsize)
        sns.heatmap(corr, annot=annot, fmt=".2f", cmap=cmap,
                    linewidths=0.5, ax=ax, square=True,
                    cbar_kws={"shrink": 0.8})
        ax.set_title(title if title else "Correlation Heatmap", fontsize=14)
        plt.tight_layout()
        plt.show()
        print("Heatmap plotted successfully")

    # ─────────────────────────────────────────
    # SUMMARY
    # ─────────────────────────────────────────

    def summary(self):
        """Print a quick summary of the loaded dataset."""
        print("=" * 40)
        print("DATASET SUMMARY")
        print("=" * 40)
        print(f"Rows        : {self.df.shape[0]}")
        print(f"Columns     : {self.df.shape[1]}")
        print(f"Missing     : {self.df.isnull().sum().sum()}")
        print(f"Numeric cols: {len(self.df.select_dtypes(include='number').columns)}")
        print(f"Text cols   : {len(self.df.select_dtypes(include='object').columns)}")
        print("=" * 40)
