"""adding foreign key to posts

Revision ID: 41f6acb42a04
Revises: 964734598474
Create Date: 2026-06-16 23:53:56.381674

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '41f6acb42a04'
down_revision: Union[str, Sequence[str], None] = '964734598474'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users", local_cols=["user_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
   op.drop_constraint('posts_users_fk', table_name="posts")
   op.drop_column('posts', 'user_id')
   pass
