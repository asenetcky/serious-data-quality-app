import marimo

__generated_with = "0.15.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("""# How many Peppers would you rate this Data Quality Right now?""")
    return


@app.cell
def _(mo):
    slider = mo.ui.slider(1, 100)
    return (slider,)


@app.cell
def _(mo, peppers):
    mo.md(f"""# Your Pepper rating is {peppers}""")
    return


@app.cell
def _(mo, slider):
    mo.md(f"""## Please select your pepper rating for these data: {slider}""")
    return


@app.cell
def _(mo, slider):
    peppers = f"{mo.icon('noto-v1:hot-pepper')}" * slider.value
    return (peppers,)


if __name__ == "__main__":
    app.run()
