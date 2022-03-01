"""create users table

Revision ID: 8e019750c5be
Revises: 6fc13a85daa2
Create Date: 2022-02-28 17:51:42.908005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e019750c5be'
down_revision = '6fc13a85daa2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=False), nullable=False, server_default=sa.func.now())
    )
    pass


def downgrade():
    op.drop_table('users')
    pass
