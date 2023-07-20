import matplotlib.pyplot as plt
import tikzplotlib
import numpy as np


def tikzplotlib_fix_ncols(obj):
    """
    workaround for matplotlib 3.6 renamed legend's _ncol to _ncols, which breaks tikzplotlib
    """
    if hasattr(obj, "_ncols"):
        print('ok')
        obj._ncol = obj._ncols
    for child in obj.get_children():
        tikzplotlib_fix_ncols(child)


values = {
    "zeros":
        {
            10: np.array([0.09144914, 0.09221112, 0.09178256, 0.09034689, 0.08946969]),
            20: np.array([0.09056374, 0.09101801, 0.09007224, 0.09079565, 0.08993510]),
            30: np.array([0.08703498, 0.08982417, 0.08927867, 0.08890105, 0.08900513]),
            40: np.array([0.08810981, 0.08617235, 0.08613121, 0.08819087, 0.08728526]),
            50: np.array([0.08462660, 0.08480452, 0.08575371, 0.08500031, 0.08369700]),
            60: np.array([0.08221981, 0.08336150, 0.08237703, 0.08221981, 0.07845755]),
            70: np.array([0.08141241, 0.08573229, 0.07889297, 0.08003416, 0.08365243]),
            80: np.array([0.07925418, 0.07934590, 0.07907970, 0.08035681, 0.08141841]),
            90: np.array([0.07930855, 0.07944569, 0.08033415, 0.07886836, 0.08084536])
        },
    "mean":
        {
            10: np.array([0.09175770, 0.09273396, 0.09208684, 0.09030403, 0.09034995]),
            20: np.array([0.09034946, 0.09070088, 0.09137812, 0.09083422, 0.09009073]),
            30: np.array([0.08864208, 0.08857535, 0.08841592, 0.08810565, 0.08814238]),
            40: np.array([0.08639129, 0.08636606, 0.08698833, 0.08828087, 0.08654214]),
            50: np.array([0.08272380, 0.08513279, 0.08510659, 0.08335586, 0.08369149]),
            60: np.array([0.08301693, 0.08233724, 0.08277817, 0.08237740, 0.07962446]),
            70: np.array([0.08048537, 0.08365500, 0.07779500, 0.07969131, 0.08064823]),
            80: np.array([0.08067186, 0.08046872, 0.07697596, 0.07763546, 0.07958540]),
            90: np.array([0.07945683, 0.07871714, 0.07685168, 0.07961895, 0.07781288])
        }
}

mean_std = {
    "zeros": {
        "x": np.array([10, 20, 30, 40, 50, 60, 70, 80, 90]),
        "y": np.array([np.mean(value) for _, value in values["zeros"].items()]),
        "std": np.array([np.std(value) for _, value in values["zeros"].items()])
    },
    "mean": {
        "x": np.array([10, 20, 30, 40, 50, 60, 70, 80, 90]),
        "y": np.array([np.mean(value) for _, value in values["mean"].items()]),
        "std": np.array([np.std(value) for _, value in values["mean"].items()])
    }
}

fig = plt.subplots(figsize=(10, 7))
plt.errorbar(mean_std["mean"]["x"], mean_std["mean"]["y"], mean_std["mean"]["std"])
plt.legend(loc="upper right")
tikzplotlib_fix_ncols(fig[0])
tikzplotlib_fix_ncols(fig[1])

tikzplotlib.save(f'./MMSSL/data/rq1.tex')
