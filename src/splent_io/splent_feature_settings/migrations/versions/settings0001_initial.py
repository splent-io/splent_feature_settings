"""setting table (runtime key/value settings).

Revision ID: settings0001
Revises:
"""

import sqlalchemy as sa
from alembic import op

revision = "settings0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "setting",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("key", sa.String(length=191), nullable=False),
        sa.Column("value", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_setting_key"), "setting", ["key"], unique=True)


def downgrade():
    op.drop_index(op.f("ix_setting_key"), table_name="setting")
    op.drop_table("setting")
