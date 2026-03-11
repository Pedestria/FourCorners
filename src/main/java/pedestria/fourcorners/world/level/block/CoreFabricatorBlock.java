package pedestria.fourcorners.world.level.block;

import javax.annotation.Nullable;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.entity.BlockEntity;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.block.state.BlockState;
import pedestria.fourcorners.world.level.block.entity.CoreFabricatorBlockEntity;

public final class CoreFabricatorBlock extends FCMenuBlock {
    public CoreFabricatorBlock(BlockBehaviour.Properties properties) {
        super(properties);
    }

    @Nullable
    @Override
    public BlockEntity newBlockEntity(BlockPos pos, BlockState state) {
        return new CoreFabricatorBlockEntity(pos, state);
    }
}
