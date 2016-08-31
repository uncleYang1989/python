import os
os.environ.setdefault("R_HOME", "/Library/Frameworks/R.framework/Resources")
import rpy2.robjects as robjects

r = robjects.r
# from rpy import NO_CONVERSION
# from rpy import BASIC_CONVERSION
# set_default_mode(NO_CONVERSION)
r.library("ALL")
r.data("ALL")
r('eset <- ALL[, ALL$mol.biol %in% c("BCR/ABL", "ALL1/AF4")]')
r.library("limma")
r('f <- factor(as.character(eset$mol.biol))')
r('design <- model.matrix(~f)')
r('fit <- eBayes(lmFit(eset,design))')
r('selected  <- p.adjust(fit$p.value[, 2]) < 0.05')
r('esetSel <- eset [selected, ]')
rpy_exprs = r('exprs(esetSel)')

def patient_colour(mol_biol) :
    if mol_biol == "ALL1/AF4" :
        return "#FF0000" # Red
    else :
        return "#0000FF" # Blue
#Get r('esetSel$mol.biol') as a python list...
# set_default_mode(BASIC_CONVERSION)
patient_colours = map(patient_colour, r('esetSel$mol.biol'))

r.heatmap(rpy_exprs,
          cexRow=0.5,
          ColSideColors = patient_colours,
          col = r.topo_colors(50))