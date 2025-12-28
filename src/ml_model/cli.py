import typer
from genrate_sample_data import make_sample_data , test_import1
app = typer.Typer()

@app.command()
def help():
    print("we have just a help command")

@app.command("make-sample-data")
def generate_sample_data(n_users: int = 50):
    make_sample_data(n_users=n_users,root ="../../data/processd")
    print("data has been generated")
@app.command()
def test_import():
    test_import1()


if __name__ == "__main__":
    app()