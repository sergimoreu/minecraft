import random
import time


class House:
    def __init__(
        self,
        mc,
        i,
        j,
        k,
        pos_x,
        pos_y,
        pos_z,
        material,
        roof,
    ):
        x, y, z = mc.player.getPos()
        self.roof = roof
        self.x = x  # relative position
        self.y = y
        self.z = z
        self.i = i  # width
        self.j = j  # height
        self.k = k  # depth
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.material = material
        self.mc = mc
        # self.door = door

    def spawn(self):
        # walls
        for a in range(self.i):
            for b in range(self.j):
                for c in range(self.k):
                    if (
                        a == 0 or c == 0 or b == 0 or a == self.i - 1 or c == self.k - 1
                    ) and (
                        self.k // 2 != c or b == 0 or c == 0 or a == 0 or b == self.j
                    ):
                        self.mc.setBlock(
                            self.x + a + self.pos_x,
                            self.y + b + self.pos_y,
                            self.z + c + self.pos_z,
                            self.material,
                        )

        # roof
        for a in range(self.i):
            for c in range(self.k):
                self.mc.setBlock(
                    self.x + a + self.pos_x,
                    self.y + b - 1 + self.pos_y,
                    self.z + c + self.pos_z,
                    self.roof,
                )


class Tree:
    # Define attributes
    def __init__(
        self,
        mc,
        player_x,
        player_y,
        player_z,
        pos_x,
        pos_y,
        pos_z,
        trunk_height,
        leaves_size,
        trunk_material,
        leaves_material,
    ):
        self.mc = mc
        self.player_x = player_x
        self.player_y = player_y
        self.player_z = player_z
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.trunk_height = trunk_height
        self.leaves_size = leaves_size
        self.trunk_material = trunk_material
        self.leaves_material = leaves_material

    # Create method
    def spawn_square(self):
        if self.leaves_size % 2 == 0:
            self.leaves_size -= 1

        # Leaves
        for x in range(self.leaves_size):
            for y in range(self.leaves_size):
                for z in range(self.leaves_size):
                    self.mc.setBlock(
                        self.player_x + self.pos_x + x - self.leaves_size // 2,
                        self.player_y + self.pos_y + y + self.trunk_height - 1,
                        self.player_z + self.pos_z + z - self.leaves_size // 2,
                        self.leaves_material,
                    )

        # Trunk
        for h in range(self.trunk_height):
            self.mc.setBlock(
                self.player_x + self.pos_x,
                self.player_y + self.pos_y + h,
                self.player_z + self.pos_z,
                self.trunk_material,
            )

    # Create method
    def spawn_christmas(self):
        if self.leaves_size % 2 == 0:
            self.leaves_size -= 1

        # Leaves
        for y in range(self.leaves_size):
            for x in range(self.leaves_size):
                for z in range(self.leaves_size):
                    block_x = (self.player_x + self.pos_x + x - self.leaves_size // 2,)
                    block_y = self.player_y + self.pos_y + y + self.trunk_height - 1
                    block_z = self.player_z + self.pos_z + z - self.leaves_size // 2

                    if (
                        x >= y
                        and z >= y
                        and x < self.leaves_size - y
                        and z < self.leaves_size - y
                    ):
                        self.mc.setBlock(
                            block_x,
                            block_y,
                            block_z,
                            self.leaves_material,
                        )

        # Trunk
        for h in range(self.trunk_height):
            self.mc.setBlock(
                self.player_x + self.pos_x,
                self.player_y + self.pos_y + h,
                self.player_z + self.pos_z,
                self.trunk_material,
            )


class RandomForest:
    def __init__(
        self,
        mc,
        player_x,
        player_y,
        player_z,
        pos_x,
        pos_y,
        pos_z,
        size,
        trunk_material,
        leaves_material,
    ):
        self.mc = mc
        self.player_x = player_x
        self.player_y = player_y
        self.player_z = player_z
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.size = size
        self.trunk_material = trunk_material
        self.leaves_material = leaves_material

    def spawn(self):
        for x in range(self.size):
            for z in range(self.size):
                time.sleep(0.2)
                tree_type = random.choice(["christmas", "square"])
                trunk_height = random.randint(3, 8)
                leaves_size = random.randint(5, 7)

                x_offset = 0
                z_offset = 0
                x_offset = x * leaves_size + random.randint(-2, 2)
                z_offset = z * leaves_size + random.randint(-2, 2)

                # import pdb;pdb.set_trace()
                t = Tree(
                    self.mc,
                    self.player_x,
                    self.player_y,
                    self.player_z,
                    self.pos_x + x_offset,
                    self.pos_y,
                    self.pos_z + z_offset,
                    trunk_height,
                    leaves_size,
                    self.trunk_material,
                    self.leaves_material,
                )
                if tree_type == "square":
                    t.spawn_square()
                elif tree_type == "christmas":
                    t.spawn_christmas()
