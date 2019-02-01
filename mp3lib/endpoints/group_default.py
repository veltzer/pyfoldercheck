from pytconf.config import register_endpoint, register_function_group

from mp3lib.configs import ConfigFake

GROUP_NAME_DEFAULT = "default"
GROUP_DESCRIPTION_DEFAULT = "all pytsv commands"


def register_group_default():
    register_function_group(
            function_group_name=GROUP_NAME_DEFAULT,
            function_group_description=GROUP_DESCRIPTION_DEFAULT,
    )


@register_endpoint(
    configs=[
        ConfigFake,
    ],
    suggest_configs=[
    ],
    group=GROUP_NAME_DEFAULT,
)
def scan():
    # type: () -> None
    """
    Scan the folder
    """
    pass
