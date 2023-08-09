"""add content column to posts table

Revision ID: f9b8d6501c60
Revises: f34ac5fc6b5c
Create Date: 2023-08-06 16:54:54.656829

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f9b8d6501c60'
down_revision: Union[str, None] = 'f34ac5fc6b5c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('content', sa.String, nullable=False)
    )


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
