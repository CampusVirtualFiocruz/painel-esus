class CheckPresence:
  def checkPresence(self, row):
    pass

class PipelineModel:
  def pipelineFn(self, row):
    for i in self.list:
      # 'type i: CheckPresence'
      i.checkPresence(row)
  
  def getResponse(self):
    result=[]
    for i in self.list:
      result.append(i.toJson())
    return result