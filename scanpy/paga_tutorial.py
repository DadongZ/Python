import numpy as np
import pandas as pd
import scanpy as sc
import pylab

sc.settings.verbosity = 3
sc.logging.print_versions()
sc.settings.set_figure_params(dpi=80, facecolor='white')
results_file = 'write/pbmc3k.h5ad'

adata = sc.read_10x_mtx(
    '/mnt/d/github/python/scanpy/filtered_gene_bc_matrices/',  # the directory with the `.mtx` file
    var_names='gene_symbols',                # use gene symbols for the variable names (variables-axis index)
    cache=True)                              # write a cache file for faster subsequent reading

adata.var_names_make_unique()
sc.pl.highest_expr_genes(adata, n_top=20, show=True)

