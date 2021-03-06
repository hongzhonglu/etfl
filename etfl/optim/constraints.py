# -*- coding: utf-8 -*-
"""
.. module:: ETFL
   :platform: Unix, Windows
   :synopsis: flux balance models accounting for expression, thermodynamics, and resource allocation constraints

.. moduleauthor:: ETFL team

Constraints declarations

"""
from pytfa.optim import ReactionConstraint, GenericConstraint


class CatalyticConstraint(ReactionConstraint):
    """
    Class to represent a enzymatic constraint
    """

    prefix = 'EC_'


class ForwardCatalyticConstraint(ReactionConstraint):
    """
    Class to represent a enzymatic constraint
    """

    prefix = 'FC_'


class BackwardCatalyticConstraint(ReactionConstraint):
    """
    Class to represent a enzymatic constraint
    """

    prefix = 'BC_'


class ModelConstraint(GenericConstraint):
    """
    Class to represent a variable attached to the model
    """

    def __init__(self, model, expr, id_, **kwargs):
        GenericConstraint.__init__(self,
                                   id_= id_,
                                   expr=expr,
                                   model=model,
                                   hook=model,
                                   **kwargs)


class GeneConstraint(GenericConstraint):
    """
    Class to represent a variable attached to a enzyme
    """

    def __init__(self, gene, expr, **kwargs):
        model = gene.model

        GenericConstraint.__init__(self,
                                   expr=expr,
                                   model=model,
                                   hook=gene,
                                   **kwargs)

    @property
    def gene(self):
        return self.hook

    @property
    def id(self):
        return self.gene.id

    @property
    def model(self):
        return self.gene.model


class EnzymeConstraint(GenericConstraint):
    """
    Class to represent a variable attached to a enzyme
    """

    def __init__(self, enzyme, expr, **kwargs):
        model = enzyme.model

        GenericConstraint.__init__(self,
                                   expr=expr,
                                   model=model,
                                   hook=enzyme,
                                   **kwargs)

    @property
    def enzyme(self):
        return self.hook

    @property
    def id(self):
        return self.enzyme.id

    @property
    def model(self):
        return self.enzyme.model


class EnzymeMassBalance(EnzymeConstraint):
    """
    Class to represent a enzymatic mass balance constraint
    """

    prefix = 'EB_'

class mRNAMassBalance(GeneConstraint):
    """
    Class to represent a mRNA mass balance constraint
    """

    prefix = 'MB_'

class rRNAMassBalance(GeneConstraint):
    """
    Class to represent a mRNA mass balance constraint
    """

    prefix = 'RB_'

class tRNAMassBalance(ModelConstraint):
    """
    Class to represent a tRNA mass balance constraint
    """

    prefix = 'TB_'

class DNAMassBalance(ModelConstraint):
    """
    Class to represent a DNA mass balance constraint
    """

    prefix = 'DB_'


class SynthesisConstraint(ReactionConstraint):
    """
    Class to represent a Translation constraint
    """

    prefix = 'TR_'


class GrowthCoupling(ReactionConstraint):
    """
    Class to represent a growth capacity constraint
    """

    prefix = 'GC_'


class TotalCapacity(EnzymeConstraint):
    """
    Class to represent the total capacity of constraint of a species, e.g
    Ribosome or RNA
    """

    prefix = 'TC_'


class TotalEnzyme(TotalCapacity):
    """
    Class to represent the total amount of an enzyme species, forwards and backwards
    """

    prefix = 'TE_'


class ExpressionCoupling(GeneConstraint):

    prefix = 'EX_'


class EnzymeRatio(ModelConstraint):
    """
    Represents the availability of free enzymes, e.g ribosomes (non bound)
    R_free = 0.2*R_total
    """

    prefix = 'ER_'

class RibosomeRatio(EnzymeRatio):
    """
    (Legacy) represents the availability of free ribosomes, e.g ribosomes (non bound)
    R_free = 0.2*R_total
    """

    prefix = 'ER_'

class EnzymeDegradation(EnzymeConstraint):
    """
    v_deg = k_deg [E]
    """

    prefix = "ED_"

class mRNADegradation(GeneConstraint):
    """
    v_deg = k_deg [mRNA]
    """

    prefix = "MD_"


class GrowthChoice(ModelConstraint):
    """
    Class to represent a variable attached to a reaction
    """

    prefix = 'GR_'


class LinearizationConstraint(ModelConstraint):
    """
    Class to represent a variable attached to a reaction
    """
    @staticmethod
    def from_constraints(cons, model):
        return LinearizationConstraint(
            name = cons.name,
            expr = cons.expr,
            model = model,
            ub = cons.ub,
            lb = cons.lb,
        )

    prefix = 'LC_'

class SOS1Constraint(ModelConstraint):
    """
    Class to represent SOS 1 constraint
    """

    prefix = 'S1_'

class InterpolationConstraint(ModelConstraint):
    """
    Class to represent an interpolation constraint
    """

    prefix = "IC_"


class EnzymeDeltaPos(EnzymeConstraint):
    """
    Represents a positive enzyme concentration variation for dETFL
    """

    prefix = 'dEP_'

class EnzymeDeltaNeg(EnzymeConstraint):
    """
    Represents a negative enzyme concentration variation for dETFL
    """

    prefix = 'dEN_'


class mRNADeltaPos(GeneConstraint):
    """
    Represents a positive mRNA concentration variation for dETFL
    """

    prefix = 'dMP_'

class mRNADeltaNeg(GeneConstraint):
    """
    Represents a negative mRNA concentration variation for dETFL
    """

    prefix = 'dMN_'