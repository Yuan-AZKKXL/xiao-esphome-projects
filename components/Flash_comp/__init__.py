import esphome.codegen as cg
import esphome.config_validation as cv
from esphome import pins  #如果需要定义引脚的话需要这个，但我这没用到
from esphome.const import CONF_ID

flash_comp_ns = cg.esphome_ns.namespace('flash_component')  #获取命名空间
Flash_comp = flash_comp_ns.class_('Flash_comp', cg.Component)  #获取命名空间里的类

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(Flash_comp), #这里对应配置文件中我们需要设置的id
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):  #此方法用于自动在main.cpp中生成初始化代码，如果没有其它参数需要传递的话直接照这么写就行
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
