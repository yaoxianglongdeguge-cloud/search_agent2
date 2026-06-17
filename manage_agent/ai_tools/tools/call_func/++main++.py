from pathlib import Path
import json

def call_func(steps:dict):
   """该工具函数用于把生成好的工作流程发给执行程序"""
   """dict：管家agent生成的工作流程"""
   current_dir=Path(__file__).parent.parent.parent.parent.parent

   with open("agent_call_queue.json",'w',encoding='utf-8') as f:
      json.dump(steps,f,ensure_ascii=False, indent=2)

   

