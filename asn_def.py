from cse6040_devkit import assignment, utils, plugins

bp = assignment.AssignmentBlueprint()

builder = assignment.AssignmentBuilder()
builder.register_blueprint(bp)

builder.build()
