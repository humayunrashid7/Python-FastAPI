"""initial

Revision ID: 6fc13a85daa2
Revises: 
Create Date: 2022-02-27 12:48:19.864292

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6fc13a85daa2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('content', sa.String(), nullable=False),
        sa.Column('published', sa.Boolean(), server_default='True'),
        sa.Column('created_at', sa.DateTime(timezone=False), nullable=False, server_default=sa.func.now())
    )
    pass


def downgrade():
    op.drop_table('posts')
    pass
