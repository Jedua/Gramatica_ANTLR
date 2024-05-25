# Generated from /content/drive/MyDrive/UAM/Teoria_Automatas_Lenguajes/Colab/Ejemplo.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,61,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,26,8,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,39,8,2,1,2,1,2,1,
        2,1,2,1,2,1,2,5,2,47,8,2,10,2,12,2,50,9,2,1,3,1,3,1,3,1,3,1,4,1,
        4,1,4,1,4,1,4,1,4,0,1,4,5,0,2,4,6,8,0,1,1,0,11,12,63,0,13,1,0,0,
        0,2,25,1,0,0,0,4,38,1,0,0,0,6,51,1,0,0,0,8,55,1,0,0,0,10,12,3,2,
        1,0,11,10,1,0,0,0,12,15,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,1,
        1,0,0,0,15,13,1,0,0,0,16,17,3,4,2,0,17,18,5,1,0,0,18,26,1,0,0,0,
        19,20,3,6,3,0,20,21,5,1,0,0,21,26,1,0,0,0,22,23,3,8,4,0,23,24,5,
        1,0,0,24,26,1,0,0,0,25,16,1,0,0,0,25,19,1,0,0,0,25,22,1,0,0,0,26,
        3,1,0,0,0,27,28,6,2,-1,0,28,39,5,10,0,0,29,39,5,11,0,0,30,31,5,4,
        0,0,31,32,3,4,2,0,32,33,5,5,0,0,33,39,1,0,0,0,34,35,5,6,0,0,35,36,
        3,4,2,0,36,37,5,7,0,0,37,39,1,0,0,0,38,27,1,0,0,0,38,29,1,0,0,0,
        38,30,1,0,0,0,38,34,1,0,0,0,39,48,1,0,0,0,40,41,10,6,0,0,41,42,5,
        2,0,0,42,47,3,4,2,7,43,44,10,5,0,0,44,45,5,3,0,0,45,47,3,4,2,6,46,
        40,1,0,0,0,46,43,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,
        0,49,5,1,0,0,0,50,48,1,0,0,0,51,52,5,11,0,0,52,53,5,8,0,0,53,54,
        3,4,2,0,54,7,1,0,0,0,55,56,5,9,0,0,56,57,5,4,0,0,57,58,7,0,0,0,58,
        59,5,5,0,0,59,9,1,0,0,0,5,13,25,38,46,48
    ]

class EjemploParser ( Parser ):

    grammarFileName = "Ejemplo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'+'", "'*'", "'('", "')'", "'['", 
                     "']'", "'='", "'print'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMERO", "ID", "STRING", 
                      "ESPACIOS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_expresion = 2
    RULE_asignacion = 3
    RULE_impresion = 4

    ruleNames =  [ "programa", "sentencia", "expresion", "asignacion", "impresion" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    NUMERO=10
    ID=11
    STRING=12
    ESPACIOS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EjemploParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(EjemploParser.SentenciaContext,i)


        def getRuleIndex(self):
            return EjemploParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = EjemploParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3664) != 0):
                self.state = 10
                self.sentencia()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(EjemploParser.ExpresionContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(EjemploParser.AsignacionContext,0)


        def impresion(self):
            return self.getTypedRuleContext(EjemploParser.ImpresionContext,0)


        def getRuleIndex(self):
            return EjemploParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)




    def sentencia(self):

        localctx = EjemploParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.expresion(0)
                self.state = 17
                self.match(EjemploParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.asignacion()
                self.state = 20
                self.match(EjemploParser.T__0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.impresion()
                self.state = 23
                self.match(EjemploParser.T__0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(EjemploParser.NUMERO, 0)

        def ID(self):
            return self.getToken(EjemploParser.ID, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EjemploParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(EjemploParser.ExpresionContext,i)


        def getRuleIndex(self):
            return EjemploParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EjemploParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expresion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 28
                self.match(EjemploParser.NUMERO)
                pass
            elif token in [11]:
                self.state = 29
                self.match(EjemploParser.ID)
                pass
            elif token in [4]:
                self.state = 30
                self.match(EjemploParser.T__3)
                self.state = 31
                self.expresion(0)
                self.state = 32
                self.match(EjemploParser.T__4)
                pass
            elif token in [6]:
                self.state = 34
                self.match(EjemploParser.T__5)
                self.state = 35
                self.expresion(0)
                self.state = 36
                self.match(EjemploParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 48
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 46
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = EjemploParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 40
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 41
                        self.match(EjemploParser.T__1)
                        self.state = 42
                        self.expresion(7)
                        pass

                    elif la_ == 2:
                        localctx = EjemploParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 43
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 44
                        self.match(EjemploParser.T__2)
                        self.state = 45
                        self.expresion(6)
                        pass

             
                self.state = 50
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(EjemploParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(EjemploParser.ExpresionContext,0)


        def getRuleIndex(self):
            return EjemploParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = EjemploParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(EjemploParser.ID)
            self.state = 52
            self.match(EjemploParser.T__7)
            self.state = 53
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(EjemploParser.STRING, 0)

        def ID(self):
            return self.getToken(EjemploParser.ID, 0)

        def getRuleIndex(self):
            return EjemploParser.RULE_impresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImpresion" ):
                listener.enterImpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImpresion" ):
                listener.exitImpresion(self)




    def impresion(self):

        localctx = EjemploParser.ImpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_impresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(EjemploParser.T__8)
            self.state = 56
            self.match(EjemploParser.T__3)
            self.state = 57
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 58
            self.match(EjemploParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




