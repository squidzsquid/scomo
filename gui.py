"""Simple form-based UI to capture some text, numerical and date fields from a user"""

import sys

from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QDateEdit,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QGroupBox,
    QLabel,
    QLineEdit,
    QSpinBox,
    QVBoxLayout,
)


# Defining a class for the GUI keeps the layout and functionality together in the same place
class GUI(QDialog):

    def __init__(self, on_submit):
        """Essentially initialise an instance of QDialog, but specialised for the GUI that we want"""
        super(GUI, self).__init__()

        self.on_submit = on_submit
        self._fields = {}

        self.setWindowTitle("App Title")
        self.setGeometry(100, 100, 300, 400)  # Essentially arbitrary, could be any size really
        self.formGroupBox = QGroupBox("Enter data:")
        self.formLayout = QFormLayout()
        self._create_form()
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self._submit_data)  # call _submit data function when the OK button is clicked
        self.buttonBox.rejected.connect(self.reject)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.formGroupBox)
        main_layout.addWidget(self.buttonBox)
        self.setLayout(main_layout)

    @staticmethod
    def _create_multi_choice(options):
        """Simple utility to create a multiple choice field in one step"""

        multi_choice_box = QComboBox()
        multi_choice_box.addItems(options)

        return multi_choice_box

    def _add_field(self, name, element):
        """Add a field to the GUI, and store a reference to it, so we can retrieve its data later on"""

        self.formLayout.addRow(QLabel(name), element)
        self._fields[name] = element

    def _create_form(self):
        """Add the various data fields to the GUI"""

        self._add_field("Field1", self._create_multi_choice(["A", "B", "C"]))
        self._add_field("Field2", self._create_multi_choice(["1", "2", "3"]))
        self._add_field("Field3", QLineEdit())
        self._add_field("Field4", QLineEdit())
        self._add_field("Field5", QLineEdit())
        self._add_field("Field6", QSpinBox())
        self._add_field("Field7", QSpinBox())
        self._add_field("Field8", QDateEdit())
        self._add_field("Field9", QDateEdit())

        self.formGroupBox.setLayout(self.formLayout)

    def _retrieve_data(self):
        """Retrieve a dictionary of fields:values from what has been input in the GUI"""

        return {k: v.currentText() if hasattr(v, "currentText") else v.text() for k, v in self._fields.items()}

    def _submit_data(self):
        """
            Called once the OK button is clicked: grab the data and pass it to whatever the on_submit function is
            (the backend defines this function -- it's kept separate from the GUI intentionally, for flexibility)
        """

        self.on_submit(self._retrieve_data())
        self.close()  # shut down the GUI window after submitting the data


def show(on_submit):
    """Launch the GUI window and pass it the on_submit function, to be executed once data are submitted by the user"""

    app = QApplication(sys.argv)
    window = GUI(on_submit)
    window.show()
    sys.exit(app.exec())
