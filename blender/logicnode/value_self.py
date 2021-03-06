import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from logicnode.arm_nodes import *

class SelfNode(Node, ArmLogicTreeNode):
    '''Self node'''
    bl_idname = 'SelfNodeType'
    bl_label = 'Self'
    bl_icon = 'GAME'
    
    def init(self, context):
        self.outputs.new('NodeSocketShader', "Object")

add_node(SelfNode, category='Value')
