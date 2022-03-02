"""create Votes association table

Revision ID: fa114e22d8f8
Revises: 17b8a6c326fd
Create Date: 2022-03-02 11:15:18.727338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa114e22d8f8'
down_revision = '17b8a6c326fd'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('votes',
        sa.Column('user_id', sa.Integer(), primary_key=True),
        sa.Column('post_id', sa.Integer(), primary_key=True),
        sa.Column('created_at', sa.DateTime(timezone=False), nullable=False, server_default=sa.func.now())
    )
    # Name foreign key is required to drop the constraint
    op.create_foreign_key('fk_votes_users', 'votes', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('fk_votes_posts', 'votes', 'posts', ['post_id'], ['id'], ondelete='CASCADE')
    pass


def downgrade():
    # Name of Foreign Key is REQUIRED
    op.drop_constraint('fk_votes_users', 'votes', type_='foreignkey')
    op.drop_constraint('fk_votes_posts', 'votes', type_='foreignkey')
    op.drop_table('votes')
    pass
