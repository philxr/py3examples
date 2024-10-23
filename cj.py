from enum import Enum

class CJPrinter:
    def __init__(self, prefix=None, suffix=None, *args, **kwargs):
        self.prefix, self.suffix = prefix, suffix
        self.args, self.kwargs = args, kwargs
    def GetPrefix(self, prefix=None):
        prefix = self.prefix if prefix is None else prefix
        return '' if prefix is None else str(prefix)
    def GetSuffix(self, suffix=None):
        suffix = self.suffix if suffix is None else suffix
        return '' if suffix is None else str(suffix)
    def SprintCJ(self, prefix=None, suffix=None):
        return ' '.join([self.GetPrefix(prefix), 'CJ', self.GetSuffix(suffix)])

class CJQualityPrinter(CJPrinter):
    def __init__(self, prefix=None, suffix=None, *args, **kwargs):
        CJPrinter.__init__(self, prefix, suffix, *args, **kwargs)
    def SprintCJBad(self, prefix=None):
        suffix = 'is my biatch.'
        return self.SprintCJ(prefix, suffix)
    def SprintCJOk(self, prefix=None):
        suffix = 'is meh.'
        return self.SprintCJ(prefix, suffix) 
    def SprintCJGood(self, prefix=None):
        suffix = 'is my gdamn homeboy.'
        return self.SprintCJ(prefix, suffix) 

class CJQuality(Enum):
    Bad = 1
    Ok = 2
    Good = 4

class CJQualityPrinter2(CJPrinter):
    cjQualityPrefixes = ['Yeah,', 'That guy,', 'CJ! that boy']
    cjQualitySuffixes = ['is my biatch.', 'is meh.', 'is my gdamn homeboy.']
    cjQualityStatements = [(x[0],x[1]) for x in zip(cjQualityPrefixes, cjQualitySuffixes)]
    cjQualityStatementChooser = {x[0]:x[1] for x in zip([e for e in CJQuality], cjQualityStatements)}
    def __init__(self, cjQuality=CJQuality.Ok, *args, **kwargs):
        self.quality = cjQuality
        prefix, suffix = type(self).cjQualityStatementChooser[cjQuality]
        CJQualityPrinter.__init__(self, prefix, suffix, *args, **kwargs)
    def __str__(self):
        prefix, suffix = type(self).cjQualityStatementChooser[self.quality]
        return self.SprintCJ(prefix, suffix)

def SprintCJ(cjQuality=CJQuality.Ok):
    return str(CJQualityPrinter2(cjQuality))

def PrintCJ(cjQuality=CJQuality.Good):
    print(SprintCJ(cjQuality))

def PrintCJ2(cjQuality=CJQuality.Good):
    prtVal = SprintCJ(PrintCJ2.quality) if hasattr(PrintCJ2, 'quality') else SprintCJ(cjQuality)
    print(str(prtVal))

def PrintDecorator(func):
    def retFunc(cjQuality=None, default=CJQuality.Ok, retName=False, retQuality=False):
        if not hasattr(func, 'quality'):
            func.quality = cjQuality if cjQuality is not None else default
        retVal = func.__name__ if retName is True else (func.quality if retQuality is True else None)
        retVal = func(cjQuality) if cjQuality is not None else (func(func.quality) if retVal is None else retVal)
        return retVal
    return retFunc

@PrintDecorator
def PrintCJ3(cjQuality=CJQuality.Good):
    print(SprintCJ(cjQuality))

GlobalClasses = ['CJPrinter', 'CJQualityPrinter', 'CJQuality', 'CJQualityPrinter2']
GlobalFuncs = ['SprintCJ', 'PrintCJ']
GlobalVars = ['GlobalClasses', 'GlobalFuncs', 'GlobalVars', 'GlobalNames']
GlobalNames = [] 
GlobalNames.extend(GlobalClasses)
GlobalNames.extend(GlobalFuncs)
GlobalNames.extend(GlobalVars)

