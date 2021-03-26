# -*- coding: utf-8 -*-
# Copyright (C) 2014-present Taiga Agile LLC
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from typing import Optional

from fastapi.security import OAuth2PasswordRequestForm as FastApiOAuth2PasswordRequestForm
from pydantic import BaseModel


## AUTH

class OAuth2PasswordRequestForm(FastApiOAuth2PasswordRequestForm): ...

class AccessTokenSchema(BaseModel):
    access_token: str
    token_type: str


### USER

class UserBaseSchema(BaseModel):
    id: int
    username: str
    full_name: Optional[str] = None
    is_active: bool

    class Config:
        orm_mode = True


class UserMeSchema(UserBaseSchema):
    email: Optional[str] = None

    class Config:
        orm_mode = True


class LoginSchema(AccessTokenSchema, UserMeSchema): ...