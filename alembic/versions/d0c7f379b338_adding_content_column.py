"""adding content column

Revision ID: d0c7f379b338
Revises: 889d154251ba
Create Date: 2026-06-15 21:38:49.719873

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd0c7f379b338'
down_revision: Union[str, Sequence[str], None] = '889d154251ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
