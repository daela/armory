import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from logicnode.arm_nodes import *

class TimeNode(Node, ArmLogicTreeNode):
    '''Time node'''
    bl_idname = 'TimeNodeType'
    bl_label = 'Time'
    bl_icon = 'TIME'
    
    def init(self, context):
        self.outputs.new('NodeSocketFloat', "Time")

add_node(TimeNode, category='Value')
