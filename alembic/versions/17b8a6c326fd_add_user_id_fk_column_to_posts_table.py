"""add user id fk column to posts table

Revision ID: 17b8a6c326fd
Revises: 8e019750c5be
Create Date: 2022-03-01 18:02:37.635600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17b8a6c326fd'
down_revision = '8e019750c5be'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'posts', 'users', ['user_id'], ['id'])
    pass


def downgrade():
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column('posts', 'user_id')
    pass
