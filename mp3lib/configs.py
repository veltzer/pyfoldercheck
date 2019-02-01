from pytconf.config import ParamCreator, Config


class ConfigFake(Config):
    """
    Parameters to specify input files
    """
    input_files = ParamCreator.create_list_str(
        help_string="input files",
    )
