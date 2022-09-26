import os
from datetime import datetime

import jinja2
import pdfkit
import imgkit


class LittleGlue(object):
    DEFAULT_FONT_CONFIGS = (18, 42, 20, "bold")     # (Candidate Name Size, Candidate Number Size, Spacing, Font Weight)
    DEFAULT_EXPORT_FORMAT = 'pdf'                   # PDF format (Accepted formats: pdf and jpg/jpeg)
    DEFAULT_COLOR_SCHEME = ("#ffffff", "#000000")   # (Background, Font) - Hexadecimal values

    def __init__(self, **kwargs):
        self.candidates_data = kwargs.get("candidates_data", {})
        self.export_format = kwargs.get("export_format", self.DEFAULT_EXPORT_FORMAT)
        self.color_scheme = kwargs.get("color_scheme", self.DEFAULT_COLOR_SCHEME)
        self.font_configs = kwargs.get("font_configs", self.DEFAULT_FONT_CONFIGS)

        # "Private" attributes
        # --------------------
        self.__election_type = self.__get_election_type_from_candidates_data(election_type=kwargs.get('election_type'))
        self.__html_template = self.__get_template_from_election_type()
        self.__output_html_filename = None

    def generate(self):
        """
        Main method to generate little glues based on the values passed to the class and returns generated filename
        :return: string
        """
        self.__check_template_path()
        LittleGlue.get_or_create_generated_glues_folder()
        self.__render_template()

        if self.export_format.lower() == 'pdf':
            filename = self.__generate_pdf()
        elif self.export_format.lower() in ['jpg', 'jpeg']:
            filename = self.__generate_jpg()
        elif self.export_format.lower() == 'html':
            return None
        else:
            raise ValueError("Formato de exportação incompatível.")

        return filename

    # Auxiliary Methods
    # -----------------
    def __get_election_type_from_candidates_data(self, election_type=None):
        """
        Gets election type based on number of candidates or when passed explicitly
        :return: string
        """
        if election_type:
            return election_type

        if len(self.candidates_data.keys()) >= 5:
            return "presidential"
        else:
            return "municipal"

    def __get_template_from_election_type(self):
        """
        Gets the path for the HTML template
        :return: string
        """
        return "templates/{}_template.html".format(self.__election_type)

    def __check_template_path(self):
        """
        Checks if template path exists
        :return: None
        """
        if not os.path.isfile(self.__html_template):
            raise FileNotFoundError("Template {} não existe.".format(self.__html_template))

    def __render_template(self):
        """
        Renders template variables and generates a HTML file
        :return: string
        """
        template_loader = jinja2.FileSystemLoader(searchpath="./")
        template_env = jinja2.Environment(loader=template_loader)
        template = template_env.get_template(self.__html_template)

        data = self.__get_render_data()
        output_html = template.render(data=data)
        self.__output_html_filename = self.__get_filename(extension='html')

        output_html_file = open('generated_glues/{}'.format(self.__output_html_filename), 'w')
        output_html_file.write(output_html)
        output_html_file.close()

        return output_html

    def __get_render_data(self):
        """
        Gets render data to be used on templates
        :return: dict
        """
        return {
            "candidates": self.candidates_data,
            "size": {
                "font_size_name": self.font_configs[0],
                "font_size_number": self.font_configs[1],
                "spacing": self.font_configs[2],
                "font_weight": self.font_configs[3]
            },
            "colors": {
                "background_color": self.color_scheme[0],
                "font_color": self.color_scheme[1],
            }
        }

    def __get_filename(self, extension):
        """
        Gets filename for generated files
        :return: string
        """
        now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        return "{}_{}.{}".format(self.__election_type, now, extension)

    def __generate_pdf(self):
        """
        Generates PDF file from template
        :return: string
        """
        filename_pdf = self.__get_filename(extension="pdf")
        pdfkit.from_file(
            input="generated_glues/{}".format(self.__output_html_filename),
            output_path="generated_glues/{}".format(filename_pdf)
        )
        return filename_pdf

    def __generate_jpg(self):
        """
        Generates JPG file from template
        :return: string
        """
        filename_jpg = self.__get_filename(extension="jpg")
        imgkit.from_file(
            filename="generated_glues/{}".format(self.__output_html_filename),
            output_path="generated_glues/{}".format(filename_jpg)
        )
        return filename_jpg

    # Static Methods
    # --------------
    @staticmethod
    def get_or_create_generated_glues_folder():
        """
        Checks if generated_glues folder was created on the root of the project and creates one if not
        :return: None
        """
        if not os.path.isdir("generated_glues"):
            os.mkdir("generated_glues")
