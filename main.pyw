import backend
import gui


if __name__ == "__main__":
    """
        Start the GUI, and pass it the backend function to be executed once data have been gathered
        N.B. This is a .pyw file, instead of .py, so that it will open without a terminal window
    """

    gui.show(backend.write_data)
