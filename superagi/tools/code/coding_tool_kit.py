from abc import ABC
from superagi.tools.base_tool import BaseToolKit, BaseTool
from typing import Type, List
from superagi.tools.code.write_code import CodingTool
from superagi.tools.code.write_spec import WriteSpecTool
from superagi.tools.code.write_test import WriteTestTool

class CodingToolKit(BaseToolKit, ABC):
    name: str = "CodingToolKit"
    description: str = "Coding Tool kit contains all tools related to coding tasks"

    def get_tools(self) -> List[BaseTool]:
        return [CodingTool(), WriteSpecTool(), WriteTestTool()]

    def get_env_keys(self) -> List[str]:
        return []
