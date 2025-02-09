from cse6040_devkit import assignment, utils, plugins
import numpy as np

bp = assignment.AssignmentBlueprint()

@bp.register_solution('reverse_dict')
def reverse_dict(d):
    rev_d = {v:k for k, v in d.items()}
    if len(d) != len(rev_d):
        raise ValueError
    return rev_d

@bp.register_demo('reverse_dict')
def reverse_dict_demo():
    valid_d = {'A': 1, 'B': 2, 'C': 3}
    invalid_d = {'A': 1, 'B': 2, 'C': 2}
    error_raised, rev_d = plugins.error_handler(reverse_dict)(valid_d)
    print(f'Results of `reverse_dict`(valid_d): Error Raised {error_raised}; Result {rev_d}')
    error_raised, rev_d = plugins.error_handler(reverse_dict)(invalid_d)
    print(f'Results of `reverse_dict`(invalid_d): Error Raised {error_raised}; Result {rev_d}')

@bp.register_sampler('reverse_dict', reverse_dict, 20, ('error_raised', 'rev_d'), plugin='error_handler')
def rd_sampler(rng: np.random.Generator):
    keys = list('qwertyuiopasdfghjklzxcvbnm')
    vals = np.arange(26, dtype=int)
    rng.shuffle(vals)
    rng.shuffle(keys)
    if rng.random() > 0.75:
        vals = rng.choice(vals, 26, replace=True)
    return {'d': dict(zip(keys, vals))}

builder = assignment.AssignmentBuilder()
builder.register_blueprint(bp)

builder.build()
