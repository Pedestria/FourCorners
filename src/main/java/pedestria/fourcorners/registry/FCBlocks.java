package pedestria.fourcorners.registry;

import java.util.function.Supplier;
import net.minecraft.world.level.block.BaseEntityBlock;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.DropExperienceBlock;
import net.minecraft.world.level.block.SoundType;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.material.MapColor;
import net.minecraft.util.valueproviders.UniformInt;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;
import pedestria.fourcorners.FourCorners;
import pedestria.fourcorners.world.level.block.CoreFabricatorBlock;
import pedestria.fourcorners.world.level.block.DimensionAccessorBlock;

public final class FCBlocks {
    public static final DeferredRegister<Block> BLOCKS =
            DeferredRegister.create(ForgeRegistries.BLOCKS, FourCorners.MODID);

    public static final RegistryObject<Block> AVALITE_ORE_BLOCK = registerBlock(
            "avalite_ore_block",
            () -> new DropExperienceBlock(
                    BlockBehaviour.Properties.of()
                            .mapColor(MapColor.STONE)
                            .strength(3.0F, 20.0F)
                            .sound(SoundType.METAL)
                            .lightLevel(state -> 7)
                            .requiresCorrectToolForDrops(),
                    UniformInt.of(1, 3)));

    public static final RegistryObject<Block> WISDOM_ORE_BLOCK = registerBlock(
            "wisdom_ore_block",
            () -> new DropExperienceBlock(
                    BlockBehaviour.Properties.of()
                            .mapColor(MapColor.STONE)
                            .strength(4.0F, 35.0F)
                            .sound(SoundType.METAL)
                            .lightLevel(state -> 11)
                            .requiresCorrectToolForDrops(),
                    UniformInt.of(2, 5)));

    public static final RegistryObject<Block> DIMENSION_ACCESSOR_BLOCK = registerBlock(
            "dimension_accessor_block",
            () -> new DimensionAccessorBlock(
                    BlockBehaviour.Properties.of()
                            .mapColor(MapColor.METAL)
                            .strength(3.0F, 20.0F)
                            .sound(SoundType.ANVIL)
                            .lightLevel(state -> 7)
                            .requiresCorrectToolForDrops()));

    public static final RegistryObject<Block> CORE_FABRICATOR_SIMPLE_BLOCK = registerBlock(
            "core_fabricator_simple_block",
            () -> new CoreFabricatorBlock(
                    BlockBehaviour.Properties.of()
                            .mapColor(MapColor.METAL)
                            .strength(3.0F, 20.0F)
                            .sound(SoundType.STONE)
                            .lightLevel(state -> 7)
                            .requiresCorrectToolForDrops()));

    private FCBlocks() {}

    private static RegistryObject<Block> registerBlock(String name, Supplier<Block> supplier) {
        RegistryObject<Block> block = BLOCKS.register(name, supplier);
        FCItems.registerBlockItem(name, block);
        return block;
    }
}
