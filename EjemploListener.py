# Generated from /content/drive/MyDrive/UAM/Teoria_Automatas_Lenguajes/Colab/Ejemplo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .EjemploParser import EjemploParser
else:
    from EjemploParser import EjemploParser

# This class defines a complete listener for a parse tree produced by EjemploParser.
class EjemploListener(ParseTreeListener):

    # Enter a parse tree produced by EjemploParser#programa.
    def enterPrograma(self, ctx:EjemploParser.ProgramaContext):
        pass

    # Exit a parse tree produced by EjemploParser#programa.
    def exitPrograma(self, ctx:EjemploParser.ProgramaContext):
        pass


    # Enter a parse tree produced by EjemploParser#sentencia.
    def enterSentencia(self, ctx:EjemploParser.SentenciaContext):
        pass

    # Exit a parse tree produced by EjemploParser#sentencia.
    def exitSentencia(self, ctx:EjemploParser.SentenciaContext):
        pass


    # Enter a parse tree produced by EjemploParser#expresion.
    def enterExpresion(self, ctx:EjemploParser.ExpresionContext):
        pass

    # Exit a parse tree produced by EjemploParser#expresion.
    def exitExpresion(self, ctx:EjemploParser.ExpresionContext):
        pass


    # Enter a parse tree produced by EjemploParser#asignacion.
    def enterAsignacion(self, ctx:EjemploParser.AsignacionContext):
        pass

    # Exit a parse tree produced by EjemploParser#asignacion.
    def exitAsignacion(self, ctx:EjemploParser.AsignacionContext):
        pass


    # Enter a parse tree produced by EjemploParser#impresion.
    def enterImpresion(self, ctx:EjemploParser.ImpresionContext):
        pass

    # Exit a parse tree produced by EjemploParser#impresion.
    def exitImpresion(self, ctx:EjemploParser.ImpresionContext):
        pass



del EjemploParser